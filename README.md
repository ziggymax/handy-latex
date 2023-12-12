# handy-latex-img - Docker image with LaTeX/TeX Live
This repository maintains a Dockerfile that creates an image with general and complete LaTeX/TeX Live environment. A prebuilt image gets published to Github Container Registry (ghcr.io) from which it can be pulled directly.

It is a fork of Cheng Xu's excellent project [latex-docker](https://github.com/xu-cheng/latex-docker). I found Cheng's project when I got the idea of setting up a LaTeX environment inside a container. Not very original I know, and of course somebody had already thought of that before. Using Cheng's [latex-docker](https://github.com/xu-cheng/latex-docker) together with James Yu's *very nice* [latex-workshop extension](https://github.com/James-Yu/LaTeX-Workshop) for Visual Studio Code, tied together with VSCode's amazing devcontainer feature, was a pleasure.

But I needed support for SVG graphics, and added that to the stuff already in [latex-docker](https://github.com/xu-cheng/latex-docker) (basically by simply including the Inkscape system package). Since containers should be ephemeral in general, I don't think adding extra TeX Live packages inside a container is a good idea. In addition to that, (re)building the container image just to add extra packages is cumbersome at best, so I chose to always build an image with the full TeX Live scheme, to reduce the need to add TeX Live packages. In the process of making those changes I also wanted to make the Dockerfile self-contained, rather than depend on external files.

## Pulling the image
To get a specific version use
```
docker pull ghcr.io/ziggymax/handy-latex-img:v1.0.0
```
or use
```
docker pull ghcr.io/ziggymax/handy-latex-img:latest
```
to get the latest/newest/greatest version.

## Using the image
You can of course use/abuse the contents of this repository and the associated container image as you want, subject to the terms of the license (MIT). The image produced by the Dockerfile provides a good all-round LaTeX environment. But the intention is to use the image together with:

- A container engine of some sort, such as [Docker Desktop](https://www.docker.com/products/docker-desktop/) for Windows or Mac
- [Visual Studio Code](https://code.visualstudio.com/) with these extensions installed:
    - [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) _(id: ms-vscode-remote.remote-containers)_
    - [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) _(id: james-yu.latex-workshop)_
    - Your favorite Git extensions, such as [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) _(id: eamodio.gitlens)_ and [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory) _(id: donjayamanne.githistory)_
- [Git](https://git-scm.com/) for stringent version control
- The [handy-latex-template](https://github.com/ziggymax/handy-latex-template) repository

One of the really cute features of VSCode devcontainers is that VSCode can auto-install a predefined set of extensions when you open a project/repository. So all you really have to do get started is:
1. Install Docker Desktop
1. Install VSCode with the Dev Containers extension
1. Fetch/open your project/repository

.....  and everything else happens automagically.

Look at the template repository [handy-latex-template](https://github.com/ziggymax/handy-latex-template) for more info, including an easy step-by-step guide for setting up a nice and smooooth LaTeX working environment for individual use or for working together in a team.

## License
MIT