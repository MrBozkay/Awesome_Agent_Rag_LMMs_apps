<p align="center">
  <img src="docs/research_agent_banner.png" width="100%" alt="AI Research Planner & Executor">
</p>

# 🔬 AI Research Planner & Executor Agent (Multi-Provider)

A streamlined multi-phase research agent that demonstrates stateful conversations, model mixing, and background execution. Now supports multiple LLM providers!

## 🌟 Features

-   **Multi-Provider Support**: Switch between **Google Gemini**, **OpenRouter**, **Ollama**, and **vLLM**.
-   **📋 Phase 1 - Research Planning**: Creates structured, actionable research plans.
-   **🔍 Phase 2 - Task Selection & Deep Research**:
    -   **Gemini Provider**: Leverage **Deep Research Agent** with built-in web search.
    -   **Other Providers**: Uses **DuckDuckGo Search** + LLM analysis for generic deep research.
-   **📊 Phase 3 - Synthesis**: Executive reports with findings and recommendations.
-   **🎨 Auto-Generated Infographics**: (Gemini Only) Creates whiteboard-style TL;DR summary using Gemini 3 Pro Image.
-   **🔄 Stateful Conversations**: Maintains context across phases (server-side for Gemini, client-side for others).
-   **📥 Export Reports**: Download comprehensive research reports as markdown files.

## 🎯 How It Works

```
User Goal
    ↓
[Phase 1] Planner Model → Research Plan
    ↓
[Phase 2] Select Tasks →
    (Gemini): Deep Research Agent
    (Others): DuckDuckGo Search + LLM Analysis
    ↓
[Phase 3] Synthesis Model → Executive Report
         + (Gemini Only): Image Model → TL;DR Infographic
```

## 🛠️ Tech Stack

-   **Frontend**: Streamlit
-   **LLM Integration**:
    -   `google-genai` (Official Gemini SDK)
    -   `openai` (Compatible with OpenRouter, Ollama, vLLM)
-   **Search**: `duckduckgo-search` (Fallback for non-Gemini providers)

### How to get Started?

1. Clone the GitHub repository

```bash
git clone https://github.com/MrBozkay/Awesome_Agent_Rag_LLMs_apps.git
cd advanced_ai_agents/single_agent_apps/research_agent_gemini_interaction_api
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit App

```bash
streamlit run research_planner_executor_agent.py
```

4. **Select your provider** in the sidebar:
    *   **Google Gemini**: Enter your Google API Key.
    *   **OpenRouter**: Enter API Key + Model Name.
    *   **Ollama**: Enter Base URL (default: `http://localhost:11434/v1`) + Model Name (e.g., `llama3`).
    *   **vLLM**: Enter Base URL + Key (if needed).

## 📝 Example Research Goals

-   "Research the B2B HR SaaS market in Germany - key players, regulations, pricing models"
-   "Analyze market opportunities for AI-powered customer support tools"

## ⚠️ Notes

-   **Gemini Features**: The "Interactions API" and "Deep Research" capabilities are exclusive to Google Gemini. Other providers use a custom implementation with DuckDuckGo.
-   **Deep Research**: May take 2-5 minutes for comprehensive research.

## 📄 License

Part of the [Awesome LLM Apps](https://github.com/MrBozkay/Awesome_Agent_Rag_LLMs_apps) collection.
