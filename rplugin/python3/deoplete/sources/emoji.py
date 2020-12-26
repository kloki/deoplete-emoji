from .base import Base
from .emoji import EMOJI_LIST


class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.rank = 90
        self.name = "emoji"
        self.description = "complete emoji based on the emoji code "
        self.mark = "[emoji]"
        self.filetypes = []

    def on_init(self, context):
        self.executable = context["vars"].get(
            "deoplete#sources#emoji#executable", ["emoji"]
        )

    def gather_candidates(self, context):
        return EMOJI_LIST
