print('Hi, my name is', 'Henry')

path = 'src/content/posts/hello-world.md'
f = open(path, 'w', encoding='utf-8')
f.write('---\n')
f.write('title: My First Blog Post\n')
f.write('published: 2023-09-09\n')
f.write('description: This is the first post from crawler.\n')
f.write('category: Blog\n')
f.write('tags: [Foo, Bar]\n')
f.write('draft: false\n')
f.write('---\n')
f.write('## This is a T2 title\n')
f.close()