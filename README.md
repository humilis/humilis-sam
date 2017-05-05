Humilis plug-in to deploy a SAM application
===================================================

[![PyPI](https://img.shields.io/pypi/v/humilis-sam.svg?style=flat)](https://pypi.python.org/pypi/humilis-sam)

A [humilis][humilis] plug-in layer that deploys a [SAM application][AWS SAM].

[AWS SAM]: https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md
[humilis]: https://github.com/humilis/humilis


## Installation


```
pip install humilis-sam
```


To install the development version:

```
pip install git+https://github.com/humilis/humilis-sam
```


## Development

Assuming you have [virtualenv][venv] installed:

[venv]: https://virtualenv.readthedocs.org/en/latest/

```
make develop
```

Configure humilis:

```
make configure
```


## Testing

You can test the deployment of a serverless API with:

```
make test
```

The test suite should destroy the deployed API automatically, but you
can make sure you are not leaving any infrastructure behind by manually
running:

```bash
make delete
```


## Examples

To see some examples of how to use this Humilis layer refer to the integration
tests :
```
tests/integration/humilis-sam-classic.yaml
tests/integration/humilis-sam-swagger.yaml
```

The SAM application can be deployed using a swagger file or not.
If you chose to use the swagger method, the swagger template will be generated
automatically and outputed next to your environment file.


## More information

See [humilis][humilis] documentation.

[humilis]: https://github.com/humilis/humilis/blob/master/README.md


## Contact

If you have questions, bug reports, suggestions, etc. please create an issue on
the [GitHub project page][github].

[github]: http://github.com/humilis/humilis-sam


## License

This software is licensed under the [MIT license][mit].

[mit]: http://en.wikipedia.org/wiki/MIT_License

See [License file][LICENSE].

[LICENSE]: https://github.com/humilis/humilis-sam/blob/master/LICENSE.txt


© 2017 Arnaud Charpentier, [Find Hotel][fh] and others.

[fh]: http://company.findhotel.net
