mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "[theme]
primaryColor = '#7e8f89'
backgroundColor ='#1c231e'
secondaryBackgroundColor = '#6d7871'
textColor = '#e7e8e1'
font = 'monospace'
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml