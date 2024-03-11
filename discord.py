from discord_webhook import DiscordWebhook, DiscordEmbed
import json
import requests

# Creamos el webhook y el embed, sustituyendo el enlace al webhook por el que hayamos creado en Discord
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1216767295200825515/apjpuNBGqfxAAM_lTAFzc635aR2OHACm1CMz7YSOzJyPFYqeRlxylO6LFP15ERg-0cbM")

# Creamos el embed
embed = DiscordEmbed(
    # titulo, descripcion y color del embed
    title="SAD",
    description="Hipocresía!",
    color="03b2f8")

# Añadimos la imagen del taco al mensaje
embed.set_image(url="https://images3.memedroid.com/images/UPLOADED151/641e16ad60033.jpeg")
# Añadimos el embed al webhook
webhook.add_embed(embed)
# Ejecutamos el webhook, enviando el mensaje a Discord
webhook.execute()



def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Discord Lambda!')
    }