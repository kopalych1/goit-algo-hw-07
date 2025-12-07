class Comment:
    def __init__(self, text: str, author: str):
        self.text = text
        self.author = author
        self.replies: list | None = []
        self.reply_to: Comment | None = None
        self.is_deleted: bool = False

    def add_reply(self, reply: "Comment"):

        if len(reply.replies):
            raise ValueError("Reply musn't have any replies itself")

        if self.is_deleted:
            raise ValueError("Cannot add reply to deleted comment")

        self.replies.append(reply)
        reply.reply_to = self

    def remove_reply(self):
        self.text = "-- Deleted comment --"
        self.author = "Unknown"
        self.is_deleted = True

    def __str__(self) -> str:
        if self.is_deleted:
            return f"{self.text}"
        return f"{self.author}: {self.text}"

    def __repr__(self) -> str:
        return f"{self.author}: {self.text}"

    def display(self, level=0):
        print("    " * level, self, sep='')

        if not len(self.replies):
            return

        for reply in self.replies:
            reply.display(level=level+1)



def main():

    root = Comment("Hello", "Author")

    reply1 = Comment("123", "Bot1")

    root.add_reply(reply1)
    reply1.add_reply(Comment("321", "Bot3"))

    root.add_reply(Comment("456", "Bot2"))

    reply1.remove_reply()

    root.display()


if __name__ == "__main__":
    main()
