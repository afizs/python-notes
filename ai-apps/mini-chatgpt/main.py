# app.py
import os
import streamlit as st
from typing import List, Dict, Optional

from langchain_azure_ai.chat_models import AzureAIChatCompletionsModel
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# ---------- Page setup ----------
st.set_page_config(page_title="Mini-ChatGPT", page_icon="💬")
st.title("💬 Mini-ChatGPT")


# ---------- Helpers ----------
def get_token() -> Optional[str]:
    # 1) Session token set via sidebar
    token = st.session_state.get("gh_token_input") or None

    # 2) Secrets
    if not token:
        try:
            token = st.secrets.get("GITHUB_TOKEN", None)  # type: ignore[attr-defined]
        except Exception:
            token = None

    # 3) Environment var
    if not token:
        token = os.getenv("GITHUB_TOKEN")

    return token or None


def build_messages(system_prompt: str, history: List[Dict[str, str]], user_text: str):
    msgs = []
    if system_prompt.strip():
        msgs.append(SystemMessage(content=system_prompt.strip()))
    for turn in history:
        role, content = turn["role"], turn["content"]
        if role == "user":
            msgs.append(HumanMessage(content=content))
        elif role == "assistant":
            msgs.append(AIMessage(content=content))
    msgs.append(HumanMessage(content=user_text))
    return msgs


def get_model(endpoint: str, model_name: str, credential: str):
    # Keep the constructor simple/portable; advanced params can be added if needed.
    return AzureAIChatCompletionsModel(
        endpoint=endpoint,
        model=model_name,
        credential=credential,
    )


# ---------- Sidebar: Settings ----------
with st.sidebar:
    st.header("Settings")

    # Token input (masked). Stored in session_state only.
    st.text_input(
        "GitHub Token",
        key="gh_token_input",
        type="password",
        help=(
            "A GitHub token with access to GitHub Models. "
            "Recommended scopes: `models:read` (and any required by your setup). "
            "For deployments, put it in `st.secrets` as GITHUB_TOKEN."
        ),
    )

    st.caption("We keep your token only in this browser session and never log it.")

    endpoint = st.text_input(
        "Endpoint",
        value="https://models.github.ai/inference",
        help="Default endpoint for GitHub Models.",
    )

    model_name = st.selectbox(
        "Model",
        options=[
            "openai/gpt-4.1",
            "openai/gpt-4.1-mini",
            "openai/gpt-4o",
            "openai/gpt-4o-mini",
        ],
        index=0,
        help="Pick a chat-capable model.",
    )

    system_prompt = st.text_area(
        "System Prompt (optional)",
        value="You are a concise, helpful assistant.",
        height=100,
        help="Sets behavior/tone for the assistant.",
    )

    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🧹 Clear chat"):
            st.session_state["chat_history"] = []
            st.rerun()
    with col_b:
        st.write("")  # spacer

# ---------- Session state ----------
if "chat_history" not in st.session_state:
    st.session_state[
        "chat_history"
    ] = []  # list[{"role": "user"|"assistant", "content": str}]

# ---------- Render existing chat ----------
for msg in st.session_state.chat_history:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["content"])

# ---------- Chat input ----------
user_text = st.chat_input("Type your message…")

if user_text:
    token = get_token()
    if not token:
        st.error(
            "Missing GitHub token. Add it in the sidebar, set `GITHUB_TOKEN` in environment, "
            "or provide it via `st.secrets`."
        )
    else:
        # Echo user's message in the UI and store it
        st.session_state.chat_history.append({"role": "user", "content": user_text})
        with st.chat_message("user"):
            st.markdown(user_text)

        # Call the model
        try:
            model = get_model(
                endpoint=endpoint, model_name=model_name, credential=token
            )
            msgs = build_messages(
                system_prompt, st.session_state.chat_history[:-1], user_text
            )

            with st.chat_message("assistant"):
                with st.spinner("Thinking…"):
                    response = model.invoke(msgs)
                # LangChain returns an AIMessage; content holds the text
                assistant_text = getattr(response, "content", str(response))
                st.markdown(assistant_text)

            st.session_state.chat_history.append(
                {"role": "assistant", "content": assistant_text}
            )

        except Exception as e:
            st.error(f"Request failed: {e}")
