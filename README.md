# Blog em Flask

Blog simples desenvolvido utilizando o Micro Framework Flask.

### Como  instalar o blog em seu ambiente:

```
git clone https://github.com/rorampy/blog_flask.git
cd blog_flask
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask db upgrade
flask shell
from blog.models import User
u = User(username="seu_usuario", email="seu_email")
u.set_password_hash("sua_senha")
db.session.add(u)
db.session.commit()
quit()
flask run
```

### Sugestões de melhorias:

- Log de atividades;
- Editor de texto na criação/edição do Post;
- Galeria de Imagens nos posts;
- Área de anúncios dinâmica e gerenciável;
- Múltiplos usuários;
