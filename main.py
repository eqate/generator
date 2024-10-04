import discord, asyncio, base64 as b64
from discord import app_commands
from discord.ext import commands
from config import TOKEN
from datetime import timedelta
bot_instance = commands.Bot(command_prefix="!", intents=discord.Intents.all())
cd = {}
nigger = [Channel ID HEREChannel ID HEREChannel ID HEREChannel ID HEREChannel ID HERE]  # c id
@bot_instance.event
async def on_ready():
    print(b64.b64decode("Qm90IGlzIGFsaXZl").decode())
    try:
        synced = await bot_instance.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
@bot_instance.tree.command(name="stock")
async def stock(interaction: discord.Interaction):
    try:
        with open(b64.b64decode("c3RvY2sudHh0").decode(), "r") as f:
            lines = f.readlines()
        embed = discord.Embed(title=b64.b64decode("U3RvY2s=").decode(), description=f"✅ {len(lines)} accounts", color=discord.Color.green())
        await interaction.response.send_message(embed=embed, ephemeral=True)
    except FileNotFoundError:
        await interaction.response.send_message(b64.b64decode("U3RvY2sgZmlsZSBub3QgZm91bmQh").decode(), ephemeral=True)
@bot_instance.tree.command(name="generate")
async def generate(interaction: discord.Interaction):
    user_id = interaction.user.id
    channel_id = interaction.channel_id
    if channel_id not in nigger:
        await interaction.response.send_message(f"❌ {b64.b64decode('dW5hdXRob3JpemVkIGNoYW5uZWwsIGdvIHRvIGFuIGF1dGhvcml6ZWQgY2hhbm5lbCBsaWtlIHRoZXNlOiA=').decode()}{', '.join(map(str, nigger))}", ephemeral=True)
        return
    if user_id in cd and cd[user_id] > discord.utils.utcnow():
        remaining_time = (cd[user_id] - discord.utils.utcnow()).total_seconds()
        await interaction.response.send_message(f"⏳ {b64.b64decode('d2FpdA==').decode()} {int(remaining_time)} {b64.b64decode('Y29vbGRvd24=').decode()}", ephemeral=True)
        return
    try:
        with open(b64.b64decode("c3RvY2sudHh0").decode(), "r") as f:
            lines = f.readlines()
        if lines:
            key = lines[0].strip()
            with open(b64.b64decode("c3RvY2sudHh0").decode(), "w") as f:
                f.writelines(lines[1:])
            cd[user_id] = discord.utils.utcnow() + timedelta(seconds=60)  
            await interaction.response.send_message(f"✅ {b64.b64decode('YWNjb3VudDog').decode()}`{key}`", ephemeral=True)
        else:
            await interaction.response.send_message(b64.b64decode('d2FpdCBmb3IgYSBuaWdnYSB0byByZXN0b2Nr').decode(), ephemeral=True)
    except FileNotFoundError:
        await interaction.response.send_message(b64.b64decode('Y29udGFjdCBhZG1pbiB0byByZWxlYXNlIHRoaXMgcHJvYmxlbQ==').decode(), ephemeral=True)
bot_instance.run(TOKEN)
