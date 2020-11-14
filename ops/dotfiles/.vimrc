set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

Plugin 'ludovicchabant/vim-gutentags'
Plugin 'ronakg/quickr-cscope.vim'   

Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'

Plugin 'altercation/vim-colors-solarized'

Plugin 'svermeulen/vim-easyclip'
Plugin 'tpope/vim-repeat'

Plugin 'dense-analysis/ale'

Plugin 'roxma/nvim-yarp'
Plugin 'roxma/vim-hug-neovim-rpc'
Plugin 'shougo/deoplete.nvim'
Plugin 'deoplete-plugins/deoplete-jedi'

Plugin 'ervandew/supertab'
" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

set smartindent
set number
autocmd FileType python setlocal shiftwidth=4 softtabstop=4 expandtab

set clipboard=unnamed
let g:EasyClipShareYanks=1

let b:ale_fixers = ['black']
let g:deoplete#enable_at_startup = 1
let g:deoplete#sources#jedi#show_docstring = 1
let g:jedi#goto_command = "<leader>d"
let g:jedi#goto_assignments_command = "<leader>g"
let g:jedi#goto_stubs_command = "<leader>s"
let g:jedi#goto_definitions_command = ""
let g:jedi#documentation_command = "K"
let g:jedi#usages_command = "<leader>n"
let g:jedi#completions_command = "<C-Space>"
let g:jedi#rename_command = "<leader>r"
let g:jedi#use_splits_not_buffers = "left"
let g:SuperTabDefaultCompletionType = "<c-n>"
call deoplete#custom#source('omni', 'mark', '')
autocmd FileType python setlocal completeopt-=preview

syntax enable
set background=light
let g:airline_theme='solarized'
colorscheme solarized

function! LoadCscope()
  let db = findfile("cscope.out", ".;")
  if (!empty(db))
    let path = strpart(db, 0, match(db, "/cscope.out$"))
    set nocscopeverbose " suppress 'duplicate connection' error
    exe "cs add " . db . " " . path
    set cscopeverbose
  " else add the database pointed to by environment variable 
  elseif $CSCOPE_DB != "" 
    cs add $CSCOPE_DB
  endif
endfunction
au BufEnter /* call LoadCscope()
