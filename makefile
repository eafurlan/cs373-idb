FILES :=                            \
tests.py						\
models.py						\
uml.pdf							\
apiary.apib 					\
IDB1.log						\
models.html						\
.travis.yml



check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  *.tmp
	rm -rf __pycache__

config:
	git config -l

tests:
	python3 tests.py

scrub:
	make clean
	rm -f  model.html
	rm -f  IDB1.log

models.html:
	pydoc -w models

IDB1.log:
		git log > IDB1.log

status:
	make clean
	@echo
	git branch
	git remote -v
	git status



# test: RunNetflix.tmp TestNetflix.tmp

# netflix-tests:
# 	git clone https://github.com/cs373-spring-2016/netflix-tests.git

# netflix.html: Netflix.py
# 	pydoc3 -w Netflix

# netflix.log:
# 	git log > Netflix.log

# RunNetflix.tmp: RunNetflix.in RunNetflix.out RunNetflix.py
# 	./RunNetflix.py < RunNetflix.in > RunNetflix.tmp
# 	tail -1 RunNetflix.tmp | cat

# TestNetflix.tmp: TestNetflix.py
# 	coverage3 run  --branch TestNetflix.py >  TestNetflix.tmp 2>&1
# 	coverage3 report --omit='/lusr/lib/python3.4/dist-packages/*' -m       >> TestNetflix.tmp
# 	cat TestNetflix.tmp
