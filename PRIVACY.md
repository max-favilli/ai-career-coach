# Privacy Policy

AI Career Coach runs through the host you choose, such as Claude Code or Codex. The plugin has no publisher-operated server, account system, analytics, or telemetry.

- Career profiles, job analyses, and application documents are written to the workspace you select. Keep that workspace separate from the installed plugin and avoid publishing it to a public repository.
- Prompts, attachments, file contents used by the assistant, and tool activity are processed under your host product's data controls and privacy terms. Local storage does not mean the host processes everything on your device.
- Optional employer research sends search queries and page requests through the host's browsing tools. Queries should describe the employer or role, without including private career details.
- The bundled LinkedIn scraper sends job identifiers to LinkedIn's public guest endpoint and saves retrieved postings locally. It requires optional Python dependencies. The scraper also supports user-supplied authentication cookies; these are sent to LinkedIn if explicitly configured and must never be committed or included in career documents.
- Optional PDF generation runs local browser or document-conversion tools. Installing dependencies may contact package registries and remains subject to your host's execution permissions and your authorization.

The plugin is open source under the MIT License. Its source is available at [github.com/max-favilli/ai-career-coach](https://github.com/max-favilli/ai-career-coach).
