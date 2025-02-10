program_lam = {
    "js": "자바스크립트",
    "py": "python",
    "react": "리액트",
    "html": "Hyper Text Markup Language"
}

del program_lam["html"]
# =>딕셔너리 값을 삭제할 때

for i in program_lam:
    print(program_lam[i])