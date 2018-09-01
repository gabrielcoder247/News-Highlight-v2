class Source:
	'''
	Source Class to define Source Objects
	'''
	def __init__(self,id,name,description,url,category):
		'''
		Function to initialize Source Objects
		It defines the properties each Source object will hold.
	
		Args: 
			1. id
			2. name
			3. description
			4. url 
			5. category
		'''
		self.id = id
		self.name = name
		self.description = description
		self.url = url
		self.category = category

class Article:
	'''
	Article Class to define Article Objects
	'''
	def __init__(self,name,author,title,description,url,urlToImage,publishedAt):
		'''
		Function to initialize Article Objects
		It defines the properties each Article object will hold.
	
		Args: 
			1. author
			2. title
			3. description
			4. url
			5. urlToImage
			6. date
		'''
		self.name = name
		self.author = author
		self.title = title
		self.description = description
		self.url = url
		self.urlToImage = urlToImage
		self.publishedAt = publishedAt

