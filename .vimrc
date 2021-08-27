" vim-plug settings
call plug#begin('~/.vim/plugged')

" airline plug
Plug 'vim-airline/vim-airline'

" embark colorscheme plug
Plug 'embark-theme/vim', { 'as': 'embark' }

" end vim-plug settings
call plug#end()

" enable true color support
set termguicolors

" colorscheme settings
colorscheme embark

" airline settings
let g:arline_theme = 'embark'
