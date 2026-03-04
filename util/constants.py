HF_ACCESS_TOKEN = ''
GEMINI_API_KEY = ''
ANTHROPIC_API_KEY = ''
OPENAI_API_KEY = ''

GPT_4O_MINI = 'gpt-4o-mini-2024-07-18' # OpenAI
O4_MINI = 'o4-mini-2025-04-16' # OpenAI
GPT_5 = 'gpt-5' # OpenAI
GEMINI_2_5_PRO_STABLE = 'gemini-2.5-pro' # VertexAI
GEMINI_2_5_PRO_PREVIEW = 'gemini-2.5-pro-preview-05-06' # VertexAI
CLAUDE_SONNET_4_5 = 'claude-sonnet-4-5-20250929' # Anthropic

MIME_TYPE_MAPPER = {
    '.json': 'application/json',
    '.yaml': 'application/x-yaml',
    '.yml': 'application/x-yaml',
    '.pdf': 'application/pdf',
    '.txt': 'text/plain',
    '.in': 'text/plain',
    '.ini': 'text/plain',
    '': 'text/plain',
    '.md': 'text/markdown',
    '.rst': 'text/x-rst',
    '.py': 'text/x-python',
    '.ipynb': 'application/x-ipynb+json',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.webp': 'image/webp',
}

# RGB values (in the range 0-255)
red = 0
green = 151
blue = 167

# Convert RGB values to the range 0-1
red_normalized = red / 255
green_normalized = green / 255
blue_normalized = blue / 255

# Create a tuple of normalized RGB values
# PLOT_COLOR = (red_normalized, green_normalized, blue_normalized)
PLOT_COLOR = 'C0'
