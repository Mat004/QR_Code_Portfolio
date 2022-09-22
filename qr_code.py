import qrcode

imagem = qrcode.make("https://mat004.github.io/portfolio_projetos/")

imagem.save("qr_code.jpg")
