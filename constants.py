

BASE_URL = "https://apisandbox.openbankproject.com/"
LOGIN_URL = BASE_URL + "my/logins/direct"
BALANCE_URL = BASE_URL + "obp/v4.0.0/banks/gh.29.fr/balances"
#DL_TOKEN = { 'Authorization' : 'DirectLogin token=eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.L9Jk0uuJ2Gy6u7YJ34_U45kdmkRYRLiO58V4j44Nifg', 'content-type'  : 'application/json' }

DL_TOKEN = { 'Authorization' : 'token', 'content-type'  : 'application/json' }
login_header = { 'Authorization' : 'DirectLogin username="robin.fr.29@example.com",password="c42142",consumer_key="nqlrfsdt2kmqmkd2oilelx5ykjbtty1werfl2flf"'}
