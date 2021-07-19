""" NATIVE CONFIGURATION
set nocompatible

" Show line numbers of the file
set number
set cursorline

" Set 4 space characters with the tab key
set tabstop=8 softtabstop=0 expandtab shiftwidth=4 smarttab

" Enable Syntax hightlighting
syntax on

"" Custom Config
" Add empty lines below and above the cursor
nnoremap <silent><A-j> :set paste<CR>m`o<Esc>``:set nopaste<CR>
nnoremap <silent><A-k> :set paste<CR>m`O<Esc>``:set nopaste<CR>

""" PLUGINS (managed by vim-plug)
call plug#begin()

Plug 'scrooloose/nerdTree'
Plug 'itchyny/lightline.vim'
Plug 'itchyny/vim-gitbranch'
Plug 'mhartington/oceanic-next'
Plug 'mattn/emmet-vim'
Plug 'Yggdroot/indentLine'
Plug 'tpope/vim-commentary'
Plug 'terryma/vim-multiple-cursors'

call plug#end()

"" NerdTree Config
set autochdir
let g:NERDTreeChDirMode=0
nmap <C-e> :NERDTreeToggle<CR>

"" Lightline Config
let g:lightline = {
      \ 'colorscheme': 'PaperColor',
      \ 'active': {
      \   'left': [ ['mode'],
      \             ['gitbranch', 'filename', 'modified'] ]
      \ },
      \ 'component_function': {
      \   'gitbranch': 'gitbranch#name'
      \ },
      \ }
" Show statusline all the time
set laststatus=2

"" Theme Config
if (has("termguicolors"))
    set termguicolors
endif
colorscheme OceanicNext

"" EmmetVim Config
let g:user_emmet_leader_key='<C-c>'
