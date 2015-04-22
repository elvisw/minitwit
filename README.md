>
                        / MiniTwit /

           because writing todo lists is not fun


    ~ What is MiniTwit?

      A SQLite and Flask powered twitter clone

    ~ How do I use it?

      1. edit the configuration in the minitwit.py file or
         export an MINITWIT_SETTINGS environment variable
         pointing to a configuration file.

      2. fire up a python shell and run this:

         >>> from minitwit import init_db; init_db()

      3. now you can run the minitwit.py file with your
         python interpreter and the application will
         greet you on http://localhost:5000/
	
    ~ Is it tested?

      You betcha.  Run the `minitwit_tests.py` file to
      see the tests pass.
>

#minitwit

这个应用是[flask](http://flask.pocoo.org/)的示例项目。我计划将其一步步重构，以学习flask，重构时的备忘我会放在`note.md`文件中。将来有时间的话将备忘整理成博客文章，以便大家参考。