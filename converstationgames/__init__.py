from .converstationgames import ConversationGames

def setup(bot):
    n = ConversationGames()
    bot.add_cog(n)