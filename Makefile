__init__.py: ;
	ls -1 *.py | sed -E 's/.py$$/ import */; s/^/from /' > __init__.py

clean: ;
	rm -f *.pyc

NAME = branch

branch: ;
	git checkout -b $(NAME)

MESSAGE = "Some new features"

send: ;
	git add -A
	git commit -m $(MESSAGE)
	hub fork
	hub push $(FROM) `git rev-parse --abbrev-ref HEAD`
	git log -1 --pretty=%B branch | hub pull-request -F -
