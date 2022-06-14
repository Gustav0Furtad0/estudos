
aluno = {
    "nome" : input("Digite o nome do aluno: "),
    "media" : float(input("Digite a média do aluno: "))
}

if aluno["media"] >= 7:
    aluno["situacao"] = "Aprovado"
else:
    aluno["situacao"] = "Reprovado"

print(f"{aluno['nome']} tem a média de {aluno['media']} em suas notas.")
print(f"Portanto está {aluno['situacao']}")