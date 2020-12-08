# @author: peizhenfei

test:
	cookiecutter .

clean:
	rm -rf cc_django
	pyenv uninstall cc_django
