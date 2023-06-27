import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import random
from flask import Flask
from threading import Thread
import asyncio
import chess
import chess.engine

app = Flask('')


@app.route('/')
def home():
  return "Lilichess API"


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()


keep_alive()
TOKEN = 'Your-Bot-Token'

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="!",
                      case_insensitive=True,
                      intents=intents)

#whos white
@client.command()
async def whoswhite(ctx, user1: discord.Member, user2: discord.Member):
    players = [user1, user2]
    white_player = random.choice(players)
    black_player = next(player for player in players if player != white_player)
    
    await ctx.send(f"{white_player.mention} will play as white and {black_player.mention} will play as black.")


#trying
options = {
    1: "How to create a challenge?",
    2: "How to play puzzles?",
    3: "How to join the team?",
    4: "How to play against the bot in Discord?",
    5: "How to play against Stockfish?",
    6: "How to play with friends?",
    7: "How to join a tournament?",
    8: "How to en passant?",
}
@client.command()
async def cataloge(ctx, option_number=None):
    if option_number is None:
        option_list = "\n".join([f"{key}: {value}" for key, value in options.items()])
        await ctx.send(f"Select an option by typing its number:\n{option_list}")
    else:
      try:
            selected_option = int(option_number)
            if selected_option in options:
                if selected_option == 1:
                  random_embed = discord.Embed(title="Click 'Creat game' in lichess.org")
                  random_embed.set_image(url="https://cdn.discordapp.com/attachments/1121528112136593441/1122938173404762142/image.png")
                  await ctx.reply(embed=random_embed)
                elif selected_option == 2:
                  await ctx.reply(f"https://cdn.discordapp.com/attachments/1121528112136593441/1122939793534361630/image.png")
                elif selected_option == 3:
                    await ctx.reply(f"**No team is made yet**")
                elif selected_option == 4:
                    await ctx.reply(f"https://cdn.discordapp.com/attachments/1121528112136593441/1122941237738078278/image.png")
                elif selected_option == 5:
                    await ctx.reply(f"https://cdn.discordapp.com/attachments/1121528112136593441/1122941700323692574/image.png")
                elif selected_option == 6:
                  random_embed = discord.Embed(title='Choose the color and the time control')
                  random_embed.set_image(url="https://cdn.discordapp.com/attachments/1121528112136593441/1122942900477632603/image.png")
                  await ctx.reply(embed=random_embed)
                elif selected_option == 7:
                  random_embed = discord.Embed(title="Click the tournament's link then click on join")
                  random_embed.set_image(url="https://cdn.discordapp.com/attachments/1121528112136593441/1122944354609287298/image.png")
                  await ctx.reply(embed=random_embed)
                elif selected_option == 8:      
                  await ctx.send(f"https://media.tenor.com/SY-ARkyhAioAAAAd/en-passant.gif")
                else:
                  await ctx.send("**مكانش هدا عاود خير واحد كاين**")
      except asyncio.TimeoutError:
        await ctx.send("**أيا نباتو هنا؟ راني رايحة**")




#guide
#mydzotitle
@client.command()
async def mydzotitle(ctx):
    embeds = [
        {
            'title': "DzoGM",
            'description': "Man in the pic: Bilel Bellahcene is an Algerian chess player. He holds the title of Grandmaster. Born in Strasbourg, France, he changed his federation from France to Algeria in July 2018.",
            'image': "https://cdn.discordapp.com/attachments/1122543836523151515/1122930147553718404/bilel-bellahcene-21-ans-maitre-international-du-jeu-d-echecs-chez-ses-parents-a-oberschaeffolsheim-dans-l-agglomeration-strasbourgeoise-photo-dna-eddie-rabeyrin-1582483381.png"
        },
        {
            'title': "DzoIM",
            'description': "Man in the pic: Gotham chess and IMRosen",
            'image': "https://cdn.discordapp.com/attachments/1122543836523151515/1122930955800289360/5zjgqa6r6r681.png"
        },
        {
            'title': "DzoFM",
            'description': "Man in the pic: James Canty",
            'image': "https://cdn.discordapp.com/attachments/1122543836523151515/1122932328424018070/Jimmy_Canty2017.png"
        }
          ]
    
    random_embed_data = random.choice(embeds)
    random_embed = discord.Embed(title=random_embed_data['title'], description=random_embed_data['description'])
    random_embed.set_image(url=random_embed_data['image'])
    
    await ctx.reply(embed=random_embed)
#holdagainstmagnus
@client.command()
async def againstmagnus(ctx, tag=None):
    if tag:
        number = random.randint(0, 100)
        await ctx.send(f"{tag} can hold against Magnus Carlsen for **{number}** seconds!")
    else:
        number = random.randint(0, 100)
        await ctx.send(f"You can hold against Magnus Carlsen for **{number}** seconds!")
  
#myccbot
@client.command()
async def myccbot(ctx):
    embeds = [
        {
            'title': "Martin",
            'description': "250",
            'image': "https://images.chesscomfiles.com/uploads/v1/user/66746160.794c1e49.200x200o.dbe7eab8b66c.png"
        },
        {
            'title': "The Green Pawn",
            'description': "900",
            'image': "https://images.chesscomfiles.com/uploads/v1/user/289457447.eee51980.200x200o.bc663fb3aee0.png"
        },
        {
            'title': "Deadlost",
            'description': "1300",
            'image': "https://images.chesscomfiles.com/uploads/v1/user/289476611.b0a468d1.200x200o.8b39921e264c.png"
        },
        {
            'title': "The Questionmaster",
            'description': "????",
            'image': "https://images.chesscomfiles.com/uploads/v1/user/289476547.8ebf92e2.200x200o.d0dff3a84236.png"
        },
        {
            'title': "Wally",
            'description': "1800",
            'image': "https://images.chesscomfiles.com/uploads/v1/user/66746018.e647839e.200x200o.e8412529f23b.png"
        },
        {
            'title': "Jonas",
            'description': "1700",
            'image': "https://images.chesscomfiles.com/uploads/v1/user/66746028.5a0ab39b.200x200o.8eaeab5bfbac.png"
        },
        {
            'title': "Deadlost",
            'description': "1800",
            'image': "https://images.chesscomfiles.com/uploads/v1/user/66746006.596dd0d8.200x200o.8742931b60ab.png"
        },
        {
            'title': "Wayne",
            'description': "250",
            'image': "https://images.chesscomfiles.com/uploads/v1/user/66746156.ec1ce34e.200x200o.b70323f49d6c.png"
        }
    ]
    
    random_embed_data = random.choice(embeds)
    random_embed = discord.Embed(title=random_embed_data['title'], description=random_embed_data['description'])
    random_embed.set_image(url=random_embed_data['image'])
    
    await ctx.reply(embed=random_embed)


@client.command()
async def tactics(ctx):
    tactics = [
        "Fork: A tactic where a single piece attacks two or more opponent's pieces simultaneously.",
        "Pin: A tactic where a piece is pinned to the king, preventing it from moving.",
        "Skewer: A tactic where a piece is attacked, and the piece behind it is even more valuable.",
        "Discover Attack: A tactic where a piece moves, uncovering an attack from another piece.",
        "Deflection: A tactic where a piece is lured away from its defensive position.",
        "Double Attack: A tactic where a single piece attacks two opponent's pieces at the same time.",
        "Decoy: A tactic where a piece is lured away to an unfavorable position.",
        "Trapped Piece: A tactic where a piece is trapped and unable to move or escape.",
        "Back Rank Mate: A tactic where the opponent's king is checkmated on the back rank.",
        "Sacrifice: A tactic where a piece is deliberately offered to gain a more advantageous position.",
    ]

    response = "Chess Tactics:\n\n"
    response += "\n".join([f"- {tactic}" for tactic in tactics])

    await ctx.send(response)


#gammmme
@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")

@client.command()
async def play(ctx):
    # Start a new game
    game = chess.Board()
    
    while not game.is_game_over():
        # User's move
        if game.turn == chess.WHITE:
            try:
                move = await client.wait_for("message", timeout=60, check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
                move = move.content.strip()
                move = chess.Move.from_uci(move)
                
                if move in game.legal_moves:
                    game.push(move)
                else:
                    await ctx.reply("**نقلة غير قانونية عاود صحبي**")
                    continue
            except asyncio.TimeoutError:
                await ctx.reply("**خلاص الوقتة مراحش نبات هنا**")
                break
        # Bot's move
        else:
            legal_moves = list(game.legal_moves)
            client_move = random.choice(legal_moves)
            game.push(client_move)
            await ctx.reply(f"**نلعبلك**: {client_move.uci()}")
        
        await ctx.reply(game.unicode())

    # Game over, send the result
    result_message = f"**خلصنا!** {game.result()}"
    await ctx.reply(result_message)

#top
@client.command()
async def topplayers(ctx):
    top_players = [
        "**Hadjaymen Baroud**",
        "Magnus Carlsen",
        "Firouzja, Alireza",
        "Ding Liren",
        "Ian Nepomniachtchi",
        "Nakamura, Hikaru",
        "Caruana, Fabiano",
        "Anish Giri",
        "So, Wesley",
        "Anand, Viswanathan",
        "Rapport, Richard",
    ]

    response = "Top Chess Players:\n\n"
    response += "\n".join([f"- {player}" for player in top_players])

    await ctx.send(response)

#quotes
@client.command()
async def quote(ctx):
    quotes = [
        "**Chess is the gymnasium of the mind.** - Blaise Pascal",
        "**Chess is life in miniature.** - Garry Kasparov",
        "**In chess, knowledge is a very transient thing. It changes so fast that even a single mouse-slip sometimes changes the evaluation.** - Viswanathan Anand",
        "**Chess is a sea in which a gnat may drink and an elephant may bathe.** - Indian Proverb",
        "**Chess is a beautiful mistress.** - Larsen",
        "**Every chess master was once a beginner.** - Irving Chernev",
        "**The beauty of chess is it can be whatever you want it to be. It transcends language, age, race, religion, politics, gender, and socioeconomic background. Whatever your circumstances, anyone can enjoy a good fight to the death over the chess board.** - Simon Williams",
        "**Chess is the struggle against error.** - Johannes Zukertort",
        "**Chess is the art which expresses the science of logic.** - Mikhail Botvinnik",
        "**Chess is the most elaborate waste of human intelligence outside of an advertising agency.** - Raymond Chandler"
    ]
    
    quote = random.choice(quotes)
    await ctx.send(quote)

#stats
@client.command()
async def stats(ctx, username):
    try:
        response = requests.get(f"https://lichess.org/@/{username}")
        soup = BeautifulSoup(response.text, features="html.parser")
        ratings_div = soup.find("div", {"class": "side sub-ratings"})
        
        ratings = ratings_div.find_all("a")
        rating_text = "\n".join([rating.get_text(strip=True) for rating in ratings])
        
        games_played = soup.find_all("a", {"class": "nm-item to-games"})[0]
        games_played_text = games_played.text if games_played else "N/A"
        
        stats_message = f"- User: {username}\n"
        stats_message += f"- Ratings:\n - {rating_text}\n"
        stats_message += f"- Games Played:{games_played_text}\n"
        stats_message += f"**  Brought you buy Lili  **"
        
        await ctx.send(f"```{stats_message}```")
    
    except:
        await ctx.send("Failed to retrieve user stats. Please make sure the username is valid.")
#lichess
##how many games were played
@client.command()
async def peta(ctx):
  if ctx.author.id == 765595488632045601 or ctx.author.id ==697931401550364672:
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Peta The Great"))
    openings = [
      "**3ami Peta**","**Petanon the great**","**L3ab m3a kaml el server w rba7 ||no khsar fl sa7||**", "**Chikor el-chatrange**", "**Tala3ni mod wala mtzidj tahdar m3ayi**",
      "**Ch7al tasnifak**", "**Aya parti blitz**", "**wash rak dayer fiha?**"
    ]
    random_opening = random.choice(openings)
    response = random_opening
    await ctx.send(response)
  else:
    await ctx.send("roh takhra")

@client.command()
async def ayman(ctx):
  if ctx.author.id == 765595488632045601 or ctx.author.id == 526360392335753216:
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Ayman The Great"))
    openings = [
      "**3ami Ayman**", "**Chikor el-chatrange**", "**Tala3ni mod wala mtzidj tahdar m3ayi**",
      "**Ch7al tasnifak**", "**Aya parti blitz**", "**wash rak dayer fiha?**"
    ]
    random_opening = random.choice(openings)
    response = random_opening
    await ctx.send(response)
  else:
    await ctx.send("roh takhra")



@client.command()
async def games(ctx, *, name):

  try:

    response = requests.get(f"https://lichess.org/@/{name}")
    soup = BeautifulSoup(response.text, features="html.parser")
    rating = soup.find_all("a", {"class": "nm-item to-games"})[0]

    await ctx.reply(rating.text)
  except:
    await ctx.reply("this account doesn't exist")


##rating
@client.command()
async def rating(ctx, name, rating_type):
  try:
    response = requests.get(f"https://lichess.org/@/{name}/perf/{rating_type}")
    soup = BeautifulSoup(response.text, features="html.parser")
    rating = soup.find_all("section", {"class": "glicko"})[0].text

    await ctx.reply(rating)
  except:
    await ctx.reply("**عاود اكتب الاسم راك غالط**")


##get the pgn and the moves
@client.command()
async def pgn(ctx, *, name):
  try:
    response = requests.get(name)
    soup = BeautifulSoup(response.text, features="html.parser")
    rating = soup.find_all("div", {"class": "pgn"})[0]

    await ctx.reply(rating.text)
  except:
    await ctx.reply("**عاود اكتب الاسم راك غالط**")


#remind me
@client.command()
async def t(ctx, time, *, message):
  await ctx.send(f"كاينة ثورنوا: **{message}**")
  await asyncio.sleep(int(time))
  await ctx.send(
    f"الثورنوا **{message}**رايحة تبدا , ايا الشبيبة, {ctx.author.mention}!      <@&869262994679431168>"
  )


#random chess opn
@client.command()
async def r_opn(ctx):
  openings = [
    "Italian Game", "Sicilian Defense", "Ruy Lopez", "French Defense",
    "Caro-Kann Defense", "Queen's Gambit", "King's Indian Defense",
    "Nimzo-Indian Defense", "Grünfeld Defense", "Alekhine's Defense",
    "Pirc Defense", "Scandinavian Defense", "Modern Defense", "Benoni Defense",
    "Dutch Defense", "English Opening", "Reti Opening", "Queen's Gambit",
    "Catalan Opening", "Giuoco Piano", "Vienna Game", "Philidor Defense",
    "Slav Defense", "King's Gambit", "Bird's Opening", "Nimzowitsch Defense",
    "Center Game", "Four Knights Game", "Elephant Gambit", "Danish Gambit",
    "Latvian Gambit", "Scotch Game", "Grob's Attack", "King's Indian Attack",
    "Blackmar-Diemer Gambit", "Alekhine's Gun", "Hungarian Opening",
    "Polish Opening", "Sokolsky Opening", "Colle System", "London System",
    "Stonewall Attack", "Trompowsky Attack", "Englund Gambit",
    "King's Fianchetto Opening", "Van't Kruijs Opening", "Bongcloud Opening"
  ]
  random_opening = random.choice(openings)
  response = "**جرب تلعب:  **" + random_opening
  await ctx.send(response)


#gif
@client.command()
async def lgif(ctx, *, id):
  try:
    response = (f"https://lichess1.org/game/export/gif/black/{id}.gif")
    await ctx.reply(response)
  except:
    await ctx.reply("this account doesn't exist")


#dev
@client.command()
async def dev(ctx):
  await ctx.send("The client was made by **.untitledmaster**")


client.run(TOKEN)
