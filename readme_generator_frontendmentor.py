def generate_markdown_file():
    # Prompting user for inputs
    project_name = input("Entre com o nome do projeto ")
    repository_name = input("Enter the name of your repository: ")
    link_frontendmentor = input("Enter the link to Frontend Mentor: ")
    solution_url = input("Enter the link to the solution: ")
    site_url = input("Enter the link to your site: ")

    # Prompting user to enter challenges
    user_challenges = []
    while True:
        user_challenges.append(input("Enter the name of the challenge: "))
        if input("Do you want to add another challenge? (y/n): ") == "n":
            break
    for i in range(len(user_challenges)):
        user_challenges[i] = f"- {user_challenges[i]}"
    should = "\n".join(user_challenges)

    #Tecnologies used
    tecnologies = []
    while True:
        tecnologies.append(input("Informe qual processo utilizou: ex (HTML, CSS, Flexbox, Grid) "))
        if input("Do you want to add another tecnology? (y/n): ") == "n":
            break
    for i in range(len(tecnologies)):
        tecnologies[i] = f"-{tecnologies[i]})"
    tecnologies = "\n".join(tecnologies)

    library_name = input("Entre com o nome da biblioteca JS ")
    library = input("Insira o link da biblioteca JS ")


    # Generating screnshots
    screnshot_1 = "![](https://www.frontendmentor.io/static/images/logo-mobile.svg)"
    screnshot_2 = "![](https://www.frontendmentor.io/static/images/logo-desktop.svg)"

    # Generating Markdown content
    markdown_content = f"""
# {project_name}

This is a solution to the [Product list with cart challenge on Frontend Mentor]({link_frontendmentor}). Frontend Mentor challenges help you improve your coding skills by building realistic projects. 
    
## Table of Contents
- [Overview](#overview)
    - [The challenge](#the-challenge)
    - [Screenshot](#screenshot)
    - [Links](#links)
    
## Overview
### The challenge
Users should be able to:
 {should}
    
### Screenshot
{screnshot_1}
    
{screnshot_2}

### Links
- Solution URL: ({solution_url})    
- Live Site URL: ({site_url})

## My process

### Built with
{tecnologies}
- [{library_name}]({library}) 

## Author
[Github](https://github.com/Genildocs)

[Linkedin](https://www.linkedin.com/in/genildo-cerqueira-91888786/)
    
    """

    # Writing content to Markdown file
    markdown_file_name = f"{repository_name}_README.md"
    with open(markdown_file_name, "w") as markdown_file:
        markdown_file.write(markdown_content)
    print(f"Markdown file '{markdown_file_name}' generated successfully!")






if __name__ == "__main__":
    generate_markdown_file()