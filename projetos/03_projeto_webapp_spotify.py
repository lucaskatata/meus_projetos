# %%
import os
from dotenv import load_dotenv
import streamlit as st
from requests.auth import HTTPBasicAuth
import requests

load_dotenv(override=True)

def autenticar():
    url = 'https://accounts.spotify.com/api/token'
    body = {
        'grant_type': 'client_credentials'
    }
    usuario = os.getenv('SPOTIFY_CLIENT_ID')
    senha = os.getenv('SPOTIFY_CLIENT_SECRET')
    auth = HTTPBasicAuth(username=usuario, password=senha)

    resposta = requests.post(url=url, data=body, auth=auth)

    try:
        resposta.raise_for_status()
    except requests.HTTPError as erro:
        print(f'Erro no request: {erro}')
        token = None
    else:
        token = resposta.json()['access_token']
        print('Token obtido com sucesso!')
    return token

def busca_artista(nome_artista, headers):
    url = 'https://api.spotify.com/v1/search'
    params = {
        'q': nome_artista,
        'type': 'artist'
    } 
    resposta = requests.get(url=url, headers=headers, params=params)
    try:
        primeiro_resultado = resposta.json()['artists']['items'][0]
    except IndexError:
        primeiro_resultado = None
    return primeiro_resultado

def busca_top_musicas(id_artista, headers):
    url = f'https://api.spotify.com/v1/artists/{id_artista}/top-tracks'
    resposta = requests.get(url=url, headers=headers)
    musicas = resposta.json()['tracks']
    return musicas

def main():
    st.title('Web App Spotify')
    st.write('Dados da API do Spotify (fonte: https://developer.spotify.com/documentation/web-api)')
    nome_artista = st.text_input('Busque um artista:')
    if not nome_artista:
        st.stop()
    
    token = autenticar()
    if not token:
        st.stop()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    artista = busca_artista(nome_artista=nome_artista, headers=headers)
    if not artista:
        st.warning(f'Sem dados para o artista {nome_artista}')
        st.stop()
    
    id_artista = artista['id']
    nome_artista = artista['name']
    popularidade_artista = artista['popularity']

    musicas = busca_top_musicas(id_artista=id_artista, headers=headers)

    st.subheader(f'Artista: {nome_artista} (pop: {popularidade_artista})')
    st.write('Melhores músicas:')
    for musica in musicas:
        nome_musica = musica['name']
        popularidade_musica = musica['popularity']
        link_musica = musica['external_urls']['spotify']
        link_em_markdown = f'[{nome_musica}]({link_musica})'
        st.markdown(f'{link_em_markdown}: (pop: {popularidade_musica})')

if __name__ == '__main__':
    main()