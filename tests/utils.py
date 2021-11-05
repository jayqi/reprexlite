from doctest import DocTest, DocTestParser, DocTestRunner


def cprint(*args, **kwargs):
    objs = (str(arg).replace(" ", "•") for arg in args)
    print(*objs, **kwargs)


def assert_doctest(doctest_input: str):
    examples = DocTestParser().get_examples(doctest_input)
    dt = DocTest(examples, {}, "test", None, None, None)
    result = DocTestRunner().run(dt)
    assert result.attempted > 0
    assert result.failed == 0
