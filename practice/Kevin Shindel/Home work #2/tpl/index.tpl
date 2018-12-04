$def with (context)

	<html>
		<head>
			<title>Kevin's Server</title>
		</head>
		<body>

		$if context['name']:
			I just wanted to say <em>hello</em> to $context['name'].
		$else:
			<em>Hello</em>, world!
	
		<ul>
		$for user in context['db']:
			<li>$user['name']</li>
		</ul>
		
		<form method="post" action="add">
			<label>Add</label>
			<input type="text" name="name" />
			<input type="submit" value="Add" />
		</form>

		</body>
	</html>