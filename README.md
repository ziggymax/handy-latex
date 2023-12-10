# handy-latex
This is a fork of Cheng XU's excellent project [latex-docker](https://github.com/xu-cheng/latex-docker). I found Cheng's project when I got the idea of setting up a LaTeX environment inside a container. Not very original I know, and of course somebody had thought of that before. Using Cheng's [latex-docker](https://github.com/xu-cheng/latex-docker) together with James Yu's *very nice* [latex-workshop extension](https://github.com/James-Yu/LaTeX-Workshop) for Visual Studio Code using VSCode's amazing devcontainer feature, was a pleasure.

But I needed support for using SVG graphics, so added that to [latex-docker](https://github.com/xu-cheng/latex-docker). In the process I also wanted to make the Dockerfile self-contained, rather than depend on external files. The result can be seen here. Others did all the heavy lifting, I just added SVG-support and refactored the Dockerfile (which may or may not suite your taste).

## License
MIT