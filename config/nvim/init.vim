" Required settings
set nocompatible
filetype off

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Plugin management
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()	
    Plugin 'gmarik/Vundle.vim'                           " Vundle
    Plugin 'itchyny/lightline.vim'                       " Lightline statusbar
    Plugin 'suan/vim-instant-markdown', {'rtp': 'after'} " Markdown Preview
    Plugin 'ap/vim-buftabline'                           " Buffer tabs
    " Plugin 'ryanoasis/vim-devicons'                      " Icons for Nerdtree
    Plugin 'kevinhwang91/rnvimr', {'do': 'make sync'}    " Ranger integration
    Plugin 'vimwiki/vimwiki'                             " VimWiki 
    Plugin 'tpope/vim-repeat'
    Plugin 'tpope/vim-unimpaired'
    Plugin 'tpope/vim-commentary'
    Plugin 'tpope/vim-surround'                          " Change surrounding marks
    Plugin 'vim-python/python-syntax'                    " Python highlighting
    Plugin 'ap/vim-css-color'                            " Color previews for CSS
call vundle#end()


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => General Settings
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
filetype plugin indent on       " Required
syntax enable                   " Enable syntax highlighting

set path+=**					" Searches current directory recursively.
set wildmenu					" Display all matches when tab complete.
set incsearch                   " Incremental search
set hidden                      " Needed to keep multiple buffers open
set nobackup                    " No auto backups
set noswapfile                  " No swap
set t_Co=256                    " Set if term supports 256 colors.
set number relativenumber       " Display line numbers
set clipboard=unnamedplus       " Copy/paste between vim and other programs.
set noshowmode                  " prevent non-normal modes showing in powerline and below powerline.
set laststatus=2                " Always show statusline
set expandtab                   " Use spaces instead of tabs.
set smarttab                    " Be smart using tabs ;)
set shiftwidth=4                " One tab == four spaces.
set tabstop=4                   " One tab == four spaces.
set splitbelow splitright
set guioptions-=r               "remove right-hand scroll bar
set guioptions-=L               "remove left-hand scroll bar

let g:rehash256 = 1


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Remap default keys
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" set the leader key to space
let mapleader = " "           

" vim-unimpaired movements
nmap <e <PLUG>unimpairedMoveUp
nmap >e <PLUG>unimpairedMoveDown
xmap <e <PLUG>unimpairedMoveSelectionUp
xmap >e <PLUG>unimpairedMoveSelectionDown
nmap <<space> <PLUG>unimpairedBlankUp 
nmap ><space> <PLUG>unimpairedBlankDown

" manage buffers
nmap bn :bnext<CR>
nmap bp :bprev<CR>
nmap bd :bd<CR>

" Remap splits navigation to just CTRL + hjkl
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

" Make adjusing split sizes a bit more friendly
noremap <silent> <C-Left> :vertical resize +3<CR>
noremap <silent> <C-Right> :vertical resize -3<CR>
noremap <silent> <C-Up> :resize +3<CR>
noremap <silent> <C-Down> :resize -3<CR>

" Change 2 split windows from vert to horiz or horiz to vert
map <Leader>th <C-w>t<C-w>H
map <Leader>tk <C-w>t<C-w>K


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Plugin specific settings
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Ranger
let g:rnvimr_ex_enable = 1
nmap <leader>r :RnvimrToggle<CR>

" Lightline
let g:lightline = {'colorscheme': 'darcula'}

" VimWiki
" set markdown as default syntax
let g:vimwiki_list = [{'path': '~/vimwiki/',
                      \ 'syntax': 'markdown', 'ext': '.md'}]

" Vim-Instant-Markdown
let g:instant_markdown_autostart = 0         " Turns off auto preview
let g:instant_markdown_browser = "surf"      " Uses surf for preview
map <Leader>md :InstantMarkdownPreview<CR>   " Previews .md file
map <Leader>ms :InstantMarkdownStop<CR>      " Kills the preview

" Splits
" Removes pipes | that act as seperators on splits
set fillchars+=vert:\ 

" Python syntax
let g:python_highlight_all = 1


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Colors and Theming
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
highlight LineNr           ctermfg=8    ctermbg=none    cterm=none
highlight CursorLineNr     ctermfg=7    ctermbg=8       cterm=none
highlight VertSplit        ctermfg=0    ctermbg=8       cterm=none
highlight Statement        ctermfg=2    ctermbg=none    cterm=none
highlight Directory        ctermfg=4    ctermbg=none    cterm=none
highlight StatusLine       ctermfg=7    ctermbg=8       cterm=none
highlight StatusLineNC     ctermfg=7    ctermbg=8       cterm=none
highlight Comment          ctermfg=4    ctermbg=none    cterm=none
highlight Constant         ctermfg=12   ctermbg=none    cterm=none
highlight Special          ctermfg=4    ctermbg=none    cterm=none
highlight Identifier       ctermfg=6    ctermbg=none    cterm=none
highlight PreProc          ctermfg=5    ctermbg=none    cterm=none
highlight String           ctermfg=12   ctermbg=none    cterm=none
highlight Number           ctermfg=1    ctermbg=none    cterm=none
highlight Function         ctermfg=1    ctermbg=none    cterm=none
highlight WildMenu         ctermfg=0       ctermbg=80      cterm=none
highlight Folded           ctermfg=103     ctermbg=234     cterm=none
highlight FoldColumn       ctermfg=103     ctermbg=234     cterm=none
highlight DiffAdd          ctermfg=none    ctermbg=23      cterm=none
highlight DiffChange       ctermfg=none    ctermbg=56      cterm=none
highlight DiffDelete       ctermfg=168     ctermbg=96      cterm=none
highlight DiffText         ctermfg=0       ctermbg=80      cterm=none
highlight SignColumn       ctermfg=244     ctermbg=235     cterm=none
highlight Conceal          ctermfg=251     ctermbg=none    cterm=none
highlight SpellBad         ctermfg=168     ctermbg=none    cterm=underline
highlight SpellCap         ctermfg=80      ctermbg=none    cterm=underline
highlight SpellRare        ctermfg=121     ctermbg=none    cterm=underline
highlight SpellLocal       ctermfg=186     ctermbg=none    cterm=underline
highlight Pmenu            ctermfg=251     ctermbg=234     cterm=none
highlight PmenuSel         ctermfg=244       ctermbg=none     cterm=none
highlight PmenuSbar        ctermfg=206     ctermbg=235     cterm=none
highlight PmenuThumb       ctermfg=235     ctermbg=206     cterm=none
highlight TabLine          ctermfg=244     ctermbg=none     cterm=none
highlight TablineSel       ctermfg=0       ctermbg=12     cterm=none
highlight TablineFill      ctermfg=244     ctermbg=8     cterm=none
highlight CursorColumn     ctermfg=none    ctermbg=236     cterm=none
highlight CursorLine       ctermfg=none    ctermbg=236     cterm=none
highlight ColorColumn      ctermfg=none    ctermbg=236     cterm=none
highlight Cursor           ctermfg=0       ctermbg=5       cterm=none
highlight htmlEndTag       ctermfg=114     ctermbg=none    cterm=none
highlight xmlEndTag        ctermfg=114     ctermbg=none    cterm=none
