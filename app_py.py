{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "app.py",
      "provenance": [],
      "mount_file_id": "1zP-FFwCW8aficKt_yf8tRONxdPGXtJPs",
      "authorship_tag": "ABX9TyM2xks7CsJKsuONq/jcaQgB",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/machaaki1102/page_transition/blob/main/app_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import pandas as pd\n",
        "import streamlit as st\n",
        "import numpy as np\n",
        "#import plotly_express as px\n",
        "\n",
        "\n",
        "#MIKIO KUBO のyoutubeのWEBアプリの開発https://www.youtube.com/watch?v=wAwk2180JgE\n",
        "\n",
        "st.title('パーツ一覧')\n",
        "#文字列の表示\n",
        "st.write('検索結果')\n"
      ],
      "metadata": {
        "id": "PGAt4qBNxoO8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "awev0lzczBPi",
        "outputId": "0a676b6b-41df-4fd6-edd1-53049d7a580f"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.6.0-py2.py3-none-any.whl (9.7 MB)\n",
            "\u001b[K     |████████████████████████████████| 9.7 MB 4.5 MB/s \n",
            "\u001b[?25hRequirement already satisfied: tornado>=5.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (5.1.1)\n",
            "Requirement already satisfied: attrs in /usr/local/lib/python3.7/dist-packages (from streamlit) (21.4.0)\n",
            "Requirement already satisfied: protobuf!=3.11,>=3.6.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (3.17.3)\n",
            "Collecting watchdog\n",
            "  Downloading watchdog-2.1.6-py3-none-manylinux2014_x86_64.whl (76 kB)\n",
            "\u001b[K     |████████████████████████████████| 76 kB 4.2 MB/s \n",
            "\u001b[?25hRequirement already satisfied: numpy in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.21.5)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.8.2)\n",
            "Collecting pydeck>=0.1.dev5\n",
            "  Downloading pydeck-0.7.1-py2.py3-none-any.whl (4.3 MB)\n",
            "\u001b[K     |████████████████████████████████| 4.3 MB 30.3 MB/s \n",
            "\u001b[?25hRequirement already satisfied: pyarrow in /usr/local/lib/python3.7/dist-packages (from streamlit) (6.0.1)\n",
            "Collecting pympler>=0.9\n",
            "  Downloading Pympler-1.0.1-py3-none-any.whl (164 kB)\n",
            "\u001b[K     |████████████████████████████████| 164 kB 51.2 MB/s \n",
            "\u001b[?25hCollecting blinker\n",
            "  Downloading blinker-1.4.tar.gz (111 kB)\n",
            "\u001b[K     |████████████████████████████████| 111 kB 46.1 MB/s \n",
            "\u001b[?25hRequirement already satisfied: tzlocal in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.5.1)\n",
            "Requirement already satisfied: importlib-metadata>=1.4 in /usr/local/lib/python3.7/dist-packages (from streamlit) (4.11.1)\n",
            "Requirement already satisfied: cachetools>=4.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (4.2.4)\n",
            "Collecting toml\n",
            "  Downloading toml-0.10.2-py2.py3-none-any.whl (16 kB)\n",
            "Collecting base58\n",
            "  Downloading base58-2.1.1-py3-none-any.whl (5.6 kB)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.7/dist-packages (from streamlit) (21.3)\n",
            "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (7.1.2)\n",
            "Requirement already satisfied: semver in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.13.0)\n",
            "Collecting validators\n",
            "  Downloading validators-0.18.2-py3-none-any.whl (19 kB)\n",
            "Collecting gitpython!=3.1.19\n",
            "  Downloading GitPython-3.1.27-py3-none-any.whl (181 kB)\n",
            "\u001b[K     |████████████████████████████████| 181 kB 49.3 MB/s \n",
            "\u001b[?25hRequirement already satisfied: altair>=3.2.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (4.2.0)\n",
            "Requirement already satisfied: click>=7.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (7.1.2)\n",
            "Requirement already satisfied: astor in /usr/local/lib/python3.7/dist-packages (from streamlit) (0.8.1)\n",
            "Requirement already satisfied: pandas>=0.21.0 in /usr/local/lib/python3.7/dist-packages (from streamlit) (1.3.5)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.7/dist-packages (from streamlit) (2.23.0)\n",
            "Requirement already satisfied: typing-extensions in /usr/local/lib/python3.7/dist-packages (from streamlit) (3.10.0.2)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (0.11.2)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (4.3.3)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (2.11.3)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.7/dist-packages (from altair>=3.2.0->streamlit) (0.4)\n",
            "Collecting gitdb<5,>=4.0.1\n",
            "  Downloading gitdb-4.0.9-py3-none-any.whl (63 kB)\n",
            "\u001b[K     |████████████████████████████████| 63 kB 1.4 MB/s \n",
            "\u001b[?25hCollecting smmap<6,>=3.0.1\n",
            "  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata>=1.4->streamlit) (3.7.0)\n",
            "Requirement already satisfied: importlib-resources>=1.4.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (5.4.0)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (0.18.1)\n",
            "Requirement already satisfied: pytz>=2017.3 in /usr/local/lib/python3.7/dist-packages (from pandas>=0.21.0->streamlit) (2018.9)\n",
            "Requirement already satisfied: six>=1.9 in /usr/local/lib/python3.7/dist-packages (from protobuf!=3.11,>=3.6.0->streamlit) (1.15.0)\n",
            "Requirement already satisfied: ipywidgets>=7.0.0 in /usr/local/lib/python3.7/dist-packages (from pydeck>=0.1.dev5->streamlit) (7.6.5)\n",
            "Requirement already satisfied: traitlets>=4.3.2 in /usr/local/lib/python3.7/dist-packages (from pydeck>=0.1.dev5->streamlit) (5.1.1)\n",
            "Collecting ipykernel>=5.1.2\n",
            "  Downloading ipykernel-6.9.1-py3-none-any.whl (128 kB)\n",
            "\u001b[K     |████████████████████████████████| 128 kB 51.1 MB/s \n",
            "\u001b[?25hCollecting ipython>=7.23.1\n",
            "  Downloading ipython-7.32.0-py3-none-any.whl (793 kB)\n",
            "\u001b[K     |████████████████████████████████| 793 kB 40.0 MB/s \n",
            "\u001b[?25hRequirement already satisfied: jupyter-client<8.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (5.3.5)\n",
            "Requirement already satisfied: matplotlib-inline<0.2.0,>=0.1.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.1.3)\n",
            "Requirement already satisfied: nest-asyncio in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (1.5.4)\n",
            "Requirement already satisfied: debugpy<2.0,>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (1.0.0)\n",
            "Requirement already satisfied: setuptools>=18.5 in /usr/local/lib/python3.7/dist-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (57.4.0)\n",
            "Collecting prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0\n",
            "  Downloading prompt_toolkit-3.0.28-py3-none-any.whl (380 kB)\n",
            "\u001b[K     |████████████████████████████████| 380 kB 44.3 MB/s \n",
            "\u001b[?25hRequirement already satisfied: jedi>=0.16 in /usr/local/lib/python3.7/dist-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.18.1)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.7/dist-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.4.2)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.7/dist-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.7.5)\n",
            "Requirement already satisfied: backcall in /usr/local/lib/python3.7/dist-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
            "Requirement already satisfied: pexpect>4.3 in /usr/local/lib/python3.7/dist-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.8.0)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.7/dist-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (2.6.1)\n",
            "Requirement already satisfied: widgetsnbextension~=3.5.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (3.5.2)\n",
            "Requirement already satisfied: ipython-genutils~=0.2.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
            "Requirement already satisfied: jupyterlab-widgets>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.0.2)\n",
            "Requirement already satisfied: nbformat>=4.2.0 in /usr/local/lib/python3.7/dist-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.1.3)\n",
            "Requirement already satisfied: parso<0.9.0,>=0.8.0 in /usr/local/lib/python3.7/dist-packages (from jedi>=0.16->ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.8.3)\n",
            "Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.7/dist-packages (from jinja2->altair>=3.2.0->streamlit) (2.0.1)\n",
            "Requirement already satisfied: pyzmq>=13 in /usr/local/lib/python3.7/dist-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (22.3.0)\n",
            "Requirement already satisfied: jupyter-core>=4.6.0 in /usr/local/lib/python3.7/dist-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.9.2)\n",
            "Requirement already satisfied: ptyprocess>=0.5 in /usr/local/lib/python3.7/dist-packages (from pexpect>4.3->ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.7.0)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.7/dist-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.5)\n",
            "Requirement already satisfied: notebook>=4.4.1 in /usr/local/lib/python3.7/dist-packages (from widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.3.1)\n",
            "Requirement already satisfied: nbconvert in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.6.1)\n",
            "Requirement already satisfied: terminado>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.13.1)\n",
            "Requirement already satisfied: Send2Trash in /usr/local/lib/python3.7/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.8.0)\n",
            "Requirement already satisfied: bleach in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (4.1.0)\n",
            "Requirement already satisfied: defusedxml in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.7.1)\n",
            "Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.5.0)\n",
            "Requirement already satisfied: mistune<2,>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.8.4)\n",
            "Requirement already satisfied: testpath in /usr/local/lib/python3.7/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.0)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.1)\n",
            "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from packaging->streamlit) (3.0.7)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit) (1.24.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit) (2021.10.8)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit) (3.0.4)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests->streamlit) (2.10)\n",
            "Building wheels for collected packages: blinker\n",
            "  Building wheel for blinker (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for blinker: filename=blinker-1.4-py3-none-any.whl size=13478 sha256=57e782282fe2925e4d444213a8795bf2301b2b1d56ac24f514375752f15c20b7\n",
            "  Stored in directory: /root/.cache/pip/wheels/22/f5/18/df711b66eb25b21325c132757d4314db9ac5e8dabeaf196eab\n",
            "Successfully built blinker\n",
            "Installing collected packages: prompt-toolkit, ipython, ipykernel, smmap, gitdb, watchdog, validators, toml, pympler, pydeck, gitpython, blinker, base58, streamlit\n",
            "  Attempting uninstall: prompt-toolkit\n",
            "    Found existing installation: prompt-toolkit 1.0.18\n",
            "    Uninstalling prompt-toolkit-1.0.18:\n",
            "      Successfully uninstalled prompt-toolkit-1.0.18\n",
            "  Attempting uninstall: ipython\n",
            "    Found existing installation: ipython 5.5.0\n",
            "    Uninstalling ipython-5.5.0:\n",
            "      Successfully uninstalled ipython-5.5.0\n",
            "  Attempting uninstall: ipykernel\n",
            "    Found existing installation: ipykernel 4.10.1\n",
            "    Uninstalling ipykernel-4.10.1:\n",
            "      Successfully uninstalled ipykernel-4.10.1\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "jupyter-console 5.2.0 requires prompt-toolkit<2.0.0,>=1.0.0, but you have prompt-toolkit 3.0.28 which is incompatible.\n",
            "google-colab 1.0.0 requires ipykernel~=4.10, but you have ipykernel 6.9.1 which is incompatible.\n",
            "google-colab 1.0.0 requires ipython~=5.5.0, but you have ipython 7.32.0 which is incompatible.\u001b[0m\n",
            "Successfully installed base58-2.1.1 blinker-1.4 gitdb-4.0.9 gitpython-3.1.27 ipykernel-6.9.1 ipython-7.32.0 prompt-toolkit-3.0.28 pydeck-0.7.1 pympler-1.0.1 smmap-5.0.0 streamlit-1.6.0 toml-0.10.2 validators-0.18.2 watchdog-2.1.6\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.colab-display-data+json": {
              "pip_warning": {
                "packages": [
                  "IPython",
                  "ipykernel",
                  "prompt_toolkit"
                ]
              }
            }
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "gWz0EaPBzFYY"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
