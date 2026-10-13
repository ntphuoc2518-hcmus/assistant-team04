# Answer Sources UI Design

This document resolves the design requirement in issue #9: show sources under each answer. It provides two examples and an interactive-browser-ready static mockup in [ui-sources.html](./ui-sources.html). The HTML contains no JavaScript and requires no dependencies.

## Scope and current implementation

The current `reply(question)` backend returns a string and does not provide citations. This contribution specifies the future presentation and demonstrates it with sample data; it does not change the backend contract or claim that real retrieval is implemented.

## Display rules

- Place a **Sources** section immediately below the answer it supports, inside the same answer card.
- Number sources in first-use order, starting at 1 for each answer. Reuse the same number when citing the same source again.
- Place references such as **[1]** beside the supported statement. Each reference navigates to its source entry within the answer.
- Show each source's title, type, available owner/publisher, and verification status. Add a URL and update date only when those values are actually available.
- Make titles links only when a real, validated public URL is available. Otherwise display plain text; never invent URLs or dates.
- For multiple sources, make it clear which claim each source supports.
- If there is no source, say **No verified source available.** Do not fabricate a source entry.
- Clearly mark development fixtures as **Sample data — not verified**. A sample source is not evidence of official university information.
- On narrow screens, stack source entries vertically and wrap long titles and URLs. Citation links must support keyboard navigation and a visible focus indicator.
- Future rendering must escape untrusted text, validate external links, and avoid displaying secrets, personal data, or internal filesystem paths.

## Example 1 — One source

**Question:** Where is the Training Office?

> **Assistant:** In this illustrative example, the Training Office is in room I.101. **[1]**
>
> **Sources**
>
> **[1] Sample office directory**  
> Type: CSV fixture · Owner: demo dataset  
> Status: Sample data — not verified  
> Supports: the room number in the answer.  
> URL / update date: not available.

This uses the room code from the current rule-based demo. It is an illustration, not a verified campus directory entry or a claim about the current CSV schema.

## Example 2 — Two sources

**Question:** How do I request a sample student certificate, and where can I submit it?

> **Assistant:** In this illustrative workflow, fill in the certificate request form **[1]**, then submit it to the sample Student Services desk. **[2]**
>
> **Sources**
>
> **[1] Sample certificate request guide**  
> Type: document fixture · Owner: demo dataset  
> Status: Sample data — not verified  
> Supports: completing the form.  
> URL / update date: not available.
>
> **[2] Sample Student Services directory**  
> Type: directory fixture · Owner: demo dataset  
> Status: Sample data — not verified  
> Supports: the submission location.  
> URL / update date: not available.

The process and desk are fictional examples used to demonstrate two independently cited claims.

## Future UI/backend integration

A future integration may return an answer with an ordered list of sources and claim-to-source associations. Suggested source fields are `id`, `title`, `type`, `publisher`, nullable `url`, nullable `updated_at`, and `verification_status`. The UI should use those associations to render inline references and source entries. This is a proposal, not a change to `reply(question)` in this PR.

## How to inspect

1. Open `docs/ui-sources.html` in a browser. No server or package installation is needed.
2. Check that both examples have sources directly below their answers.
3. Click or keyboard-activate each inline citation and confirm it targets the matching source in the same card.
4. Reduce the viewport to approximately 375 pixels and check that the cards and source text wrap.
5. Confirm that all fixture sources are marked unverified and have no fabricated external links.

## Acceptance checklist

- [x] Mockup documented in `docs/ui-sources.md`.
- [x] Two examples provided: one source and multiple sources.
- [x] Source placement, numbering, metadata, and missing-source behavior specified.
- [x] Standalone HTML mockup supplied for visual inspection.
- [x] Current backend behavior left unchanged.

## AI use

The initial documentation and HTML mockup were generated with an AI assistant. The PR author must inspect the rendered layout, verify citation targets, and disclose what was checked in the PR before requesting approval.
