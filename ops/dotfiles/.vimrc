set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'

Plugin 'lifepillar/vim-solarized8'

Plugin 'svermeulen/vim-easyclip'
Plugin 'tpope/vim-repeat'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

set smartindent
set number
autocmd FileType python setlocal shiftwidth=4 softtabstop=4 expandtab

set clipboard=unnamed
let g:EasyClipShareYanks=1

syntax enable
set termguicolors
set background=light
let g:airline_theme='solarized'
colorscheme solarized8
