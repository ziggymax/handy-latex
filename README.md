# handy-latex-img - Docker image with a general LaTeX environment
This is a fork of Cheng Xu's excellent project [latex-docker](https://github.com/xu-cheng/latex-docker). I found Cheng's project when I got the idea of setting up a LaTeX environment inside a container. Not very original I know, and of course somebody had already thought of that before. Using Cheng's [latex-docker](https://github.com/xu-cheng/latex-docker) together with James Yu's *very nice* [latex-workshop extension](https://github.com/James-Yu/LaTeX-Workshop) for Visual Studio Code, tied together with VSCode's amazing devcontainer feature, was a pleasure.

But I needed support for SVG graphics, and added that to the stuff already in [latex-docker](https://github.com/xu-cheng/latex-docker) (basically by simply including the Inkscape system package). Since containers should be ephemeral in general, I don't think adding extra TeX Live packages inside a container is a good idea. In addition to that, (re)building the container image just to add extra packages is cumbersome at best, so I chose to always build an image with the full TeX Live scheme, to reduce the need to add TeX Live packages. In the process of making those changes I also wanted to make the Dockerfile self-contained, rather than depend on external files.

## Using the image
You can of course use/abuse the contents of this repository as you, subject to the term of the license (MIT). The image produced by the Docker file provides a good all-round LaTeX environment. But the intention is to use the image together with:

- A container engine of some sort, such as [Docker Desktop](https://www.docker.com/products/docker-desktop/) for Windows or Mac
- [Visual Studio Code](https://code.visualstudio.com/) with these extensions:
    - [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) _(identifier: ms-vscode-remote.remote-containers)_
    - [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) _(identifier: james-yu.latex-workshop)_
- The [handy-latex-template](https://github.com/ziggymax/handy-latex-template) repository

## License
MIT