""" NATIVE CONFIGURATION
set nocompatible
set encoding=UTF-8

" Show line numbers of the file
set number
set cursorline

" Set 4 space characters with the tab key
set tabstop=8 softtabstop=0 expandtab shiftwidth=4 "smarttab

" Enable Syntax hightlighting
syntax on

" Autoindent new lines

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
Plug 'ryanoasis/vim-devicons'
Plug 'airblade/vim-gitgutter'
Plug 'neoclide/coc.nvim', {'branch':'release'}
Plug 'nvim-lua/popup.nvim'
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'
Plug 'mfussenegger/nvim-lint'

call plug#end()

"" NerdTree Config
set autochdir
let g:NERDTreeChDirMode=0
nmap <C-e> :NERDTreeToggle<CR>
let NERDTreeShowLineNumbers=1

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

"" coc.nvim
inoremap <silent><expr> <TAB>
      \ coc#pum#visible() ? coc#pum#next(1):
      \ CheckBackspace() ? "\<Tab>" :
      \ coc#refresh()
inoremap <expr><S-TAB> coc#pum#visible() ? coc#pum#prev(1) : "\<C-h>"

" Make <CR> to accept selected completion item or notify coc.nvim to format
" <C-g>u breaks current undo, please make your own choice.
inoremap <silent><expr> <CR> coc#pum#visible() ? coc#pum#confirm()
                              \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"

" nvim-lint
au BufWritePost lua require('lint').try_lint()

"filetype indent off
