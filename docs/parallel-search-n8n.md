# Web research in n8n with Parallel Search MCP

Use [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp)
to search the web and read page excerpts directly in n8n. The anonymous endpoint
needs no Parallel account or API key, and searches use Fast mode. This is useful
for researching a topic or checking documentation without launching Playwright.

Create this as a separate, manual workflow. The existing FastAPI, Bing,
Streamlit and webhook workflow continue to work as before.

## Connect the MCP Client

Use an n8n installation with the built-in
[MCP Client node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcpclient/).
Choose the standalone **MCP Client**, which runs tools as ordinary workflow steps.
An AI Agent node and a model connection are not needed for this workflow.

1. Create a new workflow and add a **Manual Trigger**.
2. Connect it to an **MCP Client** node and rename that node **Search**.
3. Configure the connection:

   | Setting | Value |
   |---|---|
   | Server Transport | HTTP Streamable |
   | MCP Endpoint URL | `https://search.parallel.ai/mcp` |
   | Authentication | Header Auth |
   | Input Mode | JSON |
   | Options → Timeout | `60000` (milliseconds) |

4. Create a **Header Auth** credential with **Name** `User-Agent` and **Value**
   `autonomous-browser-ai-agent`. Select it on the node. This identifies the
   project to the server; it contains no API key or other secret. Requests still
   use the anonymous tier.
5. Open the **Tool** list. The server exposes `web_search` and `web_fetch`.
   Select `web_search` for **Search**.

## Search for documentation

Paste this object into the node's **JSON** field:

```json
{
  "objective": "Find the official Playwright instructions for installing Chromium and its Linux system dependencies.",
  "search_queries": [
    "Playwright install Chromium Linux dependencies",
    "site:playwright.dev browsers install with-deps"
  ]
}
```

Run the workflow and open **Search**'s JSON output. Successful search results
include source URLs, titles and excerpts. The payload can appear under
`structuredContent` or in a text entry under `content`; n8n may already parse
that text as JSON. Use the returned URLs to inspect the sources.

For another topic, change both the objective and the queries. Supply at least
one query; two or three short, related queries help cover different angles.

## Read a page

Add a second **MCP Client** after **Search**, rename it **Fetch**, and use the
same connection settings and Header Auth credential. Select `web_fetch`, keep
**Input Mode** set to **JSON**, and paste:

```json
{
  "urls": ["https://playwright.dev/docs/browsers"],
  "objective": "Extract the commands for installing Chromium with Linux system dependencies.",
  "search_queries": [
    "Playwright install Chromium Linux dependencies",
    "site:playwright.dev browsers install with-deps"
  ],
  "full_content": false
}
```

This example reads a specific documentation page. To read another search result,
copy its URL from **Search** into the `urls` array yourself. Connecting the nodes
controls their execution order; it does not automatically select a search result.
Run the workflow again and inspect **Fetch** for the page's URL and excerpts.
Check any per-URL errors if a page cannot be retrieved.

For related calls, you can add a `session_id` string to both input objects.
Generate a UUID once per research session and reuse it for that session's search,
fetch and retries. Leave `model_name` unset here because this manual workflow
does not use a model.

## Using the output

This workflow displays MCP output in the n8n editor. The existing Streamlit
frontend expects `{"query": "...", "results": [{"title": "...", "link": "..."}]}`.
MCP output uses a different shape, so connecting it directly to the existing
**Respond to Webhook** node will not populate the frontend's result cards.
Keep this manual workflow separate unless you add an explicit response mapping.

The anonymous service has usage limits. If a call reports a quota limit, wait
for the indicated reset rather than repeatedly executing the workflow. Do not
treat an error or empty output as a completed search. See the
[Search MCP documentation](https://docs.parallel.ai/integrations/mcp/search-mcp)
for current limits and authenticated options for higher usage.
