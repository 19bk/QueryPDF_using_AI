# QueryPDF — Terminal Quick-Start Demo
# ---------------------------------------------------
# Renders demo/quickstart.gif using VHS by Charm.
#
# Requirements:
#   brew install charmbracelet/tap/vhs   (or see https://github.com/charmbracelet/vhs)
#   git, bash
#
# Run from the repo root:
#   vhs demo/quickstart.tape
#
# The clone runs against the live repo, so the GIF reflects current state.
# Docker steps are shown as comments so the recording stays fast (~15 s).
# ---------------------------------------------------

Output demo/quickstart.gif

Set Shell "bash"
Set FontSize 16
Set Width 1200
Set Height 520
Set Theme "Dracula"
Set Padding 30
Set TypingSpeed 50ms

# Sandbox the shell in a temp dir and clean the prompt before recording.
Hide
Type "cd $(mktemp -d) && export PS1='\\$ ' && clear"
Enter
Sleep 200ms
Show

Type "# QueryPDF: chat with your PDFs in 3 commands"
Enter
Sleep 1s

Type "git clone https://github.com/19bk/QueryPDF_using_AI.git"
Enter
Sleep 3s

Type "cd QueryPDF_using_AI"
Enter
Sleep 400ms

Type "cp .env.example .env"
Enter
Sleep 500ms

Type "cat .env.example"
Enter
Sleep 2500ms

Type "# Then: docker build -t querypdf . && docker run -p 8501:8501 querypdf"
Enter
Sleep 1500ms

Type "# Open http://localhost:8501 -> ask your PDFs anything"
Enter
Sleep 3s
