from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField(
        "Nome de Usuário", validators=[DataRequired("Campo obrigatório!")]
    )
    password = PasswordField(
        "Senha", validators=[DataRequired("Campo obrigatório")]
    )
    remember_me = BooleanField("Lembrar de mim")
    submit = SubmitField("Acessar Painel")


class PostForm(FlaskForm):
    title = StringField(
        "Título",
        validators=[
            DataRequired("Campo obrigatório"),
            Length(
                min=3,
                max=120,
                message="Certifique-se de que o título tenha entre 3 e 120 caracteres.",
            ),
        ],
    )
    description = TextAreaField(
        "Descrição",
        validators=[
            Length(
                max=240,
                message="Certifique-se de que o campo de descrição não tenha mais de 240 caracteres.",
            )
        ],
    )
    body = TextAreaField("Post", validators=[DataRequired("Campo obrigatório!")])
    image = FileField(
        "Imagem de capa", validators=[FileAllowed(["jpg", "jpeg", "png"])]
    )
    submit = SubmitField("Publicar Post")
