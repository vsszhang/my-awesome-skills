# Class Knowledge Notes

`$class-knowledge-notes` turns lesson materials into a concise, traceable course archive. It supports transcripts, recordings, slides, PDFs, Word files, and classroom photos. The default deliverable is a Markdown note; request Word when you want a `.docx`.

Notes are written in Chinese, organized by topic, and retain important original-language terms. Key knowledge points link to relevant screenshots when visuals help explain the material. The note also records teacher arrangements, assignments, class exercises, review questions with answers, and a source list.

## Archive layout

The skill uses the explicit output folder as the archive root when one is provided. Otherwise it identifies the course folder from the supplied paths. Notes are saved in that root, and selected visuals are saved under `artificial/<note-file-stem>/` with relative links from the Markdown file.

## Evidence and uncertainty

Slides, handouts, and legible photos help verify subject terms and visual facts. Recordings and transcripts capture explanations and oral announcements. Unclear transcription, missing deadlines, and source conflicts stay marked as uncertain instead of being filled in by guesswork. Source files are not moved or edited.

See [usage examples](examples.md) and the runtime [SKILL.md](../../../skills/class-knowledge-notes/SKILL.md).
