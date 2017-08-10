# By   ___                       ___     
#     /\__\                     /\__\    
#    /:/ _/_         ___       /::|  |   
#   /:/ /\  \       /|  |     /:/:|  |   
#  /:/ /::\  \     |:|  |    /:/|:|  |__ 
# /:/__\/\:\__\    |:|  |   /:/ |:| /\__\
# \:\  \ /:/  /  __|:|__|   \/__|:|/:/  /
#  \:\  /:/  /  /::::\  \       |:/:/  / 
#   \:\/:/  /   ~~~~\:\  \      |::/  /  
#    \::/  /         \:\__\     |:/  /   
#     \/__/           \/__/     |/__/
#
# 在 git add 之前, 执行:
#  ______________
# < bash clean.sh >
#  ----------------
#    \
#    ###
#    /oo\ |||
#    \  / \|/
#    /""\  I
# ()|    |(I)
#    \  /  I
#   /""""\ I
#  |      |I
#  |      |I
#   \____/ I
# -----------
# 
# 10/17/2016
# Sat Nov 12 13:38:03 2016
# 删除 emacs 的版本备份文件
find ./ -name "*.~*~" -exec rm -rf {} \;
# 删除emacs的"~"备份文件
find ./ -name "*~" -exec rm -rf {} \;
# 删除".DS_Store"文件
find ./ -name ".DS_Store" -exec rm -rf {} \;
# 删除java的"*.class"文件
find ./ -name "*.class" -exec rm -rf {} \;
# 删除python编译过的 pyc 文件
find ./ -name "*.pyc" -exec rm -rf {} \;
# 删除c编译过的 *.out 文件，自己的编译习惯，通常都是输出"a.out"
find ./ -name "*.out" -exec rm -rf {} \;
# 还有emacs 的临时文件，也不需要
find ./ -name "#*#" -exec rm -rf {} \;
# latex 相关的 aux, log, gz, toc 文件
find ./ -name "*.aux" -exec rm -rf {} \;
find ./ -name "*.gz" -exec rm -rf {} \;
find ./ -name "*.log" -exec rm -rf {} \;
find ./ -name "*.toc" -exec rm -rf {} \;

