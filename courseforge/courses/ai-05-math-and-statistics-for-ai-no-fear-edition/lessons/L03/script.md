# L03 The Dot Product: Weighted Sums and Similarity | Presenter Script

Course: AI-05 · Video: 5 min · Words: 728

## Hook
If a courier needs two minutes for every kilometre and five minutes for every stop, how long will a trip take? You can answer that in your head. Without noticing, you just did the most common calculation in machine learning.

## Explain
Last time, we learned that a vector is a list of numbers. Today we combine two vectors into one number, with the dot product. In words: multiply the matching components, then add the results.

Take a equals two, five and b equals eight, three. First components: two times eight is sixteen. Second components: five times three is fifteen. Add them: sixteen plus fifteen is thirty-one. So a dot b equals thirty-one. In NumPy, you write n p dot dot, with a and b inside.

Why does this matter? Many models predict with a weighted sum. Each feature has a weight that says how much it matters. The prediction is weight times feature, for every feature, all added together. That is exactly a dot product of weights and features.

Later, we also add a starting value called the bias. So a one-feature model reads: y equals w times x plus b. In words, the prediction is the weight times the input, plus a starting value.

The dot product also measures similarity. Imagine taste scores for spicy, sweet and sour, from zero to four. Customer A is one, two, zero. Customer B is two, four, zero. Customer C is zero, zero, three. A dot B is two plus eight plus zero, which is ten. A dot C is zero. A and B like the same things. A and C share nothing.

Recommendation systems use this idea to find similar users or products. Long vectors give bigger dot products, so people often divide by both lengths. This is called cosine similarity, and it is always between minus one and one. For A and B it is exactly one, because B is just A doubled.

Here is an everyday picture. A dot product is like a shopping bill. The quantities in your basket are the features, and the prices are the weights. Multiply each quantity by its price, add everything up, and you get one total. A prediction is the bill for one example.

## Demonstrate
Let's use it. Dewi is an operations planner for a delivery start-up in Jakarta, Indonesia. Her team estimates that each kilometre adds about two minutes, and each stop adds about five minutes. These numbers are invented for the example.

Her weight vector is two, five: minutes per kilometre, and minutes per stop. Tomorrow's first trip is eight kilometres with three stops, so the feature vector is eight, three. Picture two bars stacked on top of each other, one for distance time and one for stop time.

By hand: two times eight is sixteen minutes for distance. Five times three is fifteen minutes for stops. The total is thirty-one minutes. In code, Dewi makes two NumPy arrays, w and x, and prints n p dot of w and x. The answer is thirty-one again.

Dewi also learns to read the weights. If the trip had one more stop, the prediction would rise by five minutes, the weight for stops. Each weight tells you how much the prediction changes when its feature grows by one. You will use this same reading in the capstone.

A common mistake is to multiply the matching components and forget to add them. In NumPy, w star x gives sixteen, fifteen, which is still a vector. N p dot gives thirty-one, one number. And if the vectors have different lengths, NumPy stops with an error. That error is helpful: every feature needs exactly one weight.

## Recap
Let's recap. First, the dot product multiplies matching components and adds the results, giving one number. Second, a model's prediction is often a weighted sum of features, which is a dot product of weights and features. Third, a large dot product, or a cosine similarity close to one, means two vectors point in a similar direction, and zero means they share nothing.

## CTA
Your turn. In the exercise, you calculate three dot products by hand, check them with n p dot, and make a price prediction for a small invented product. It takes about twenty minutes. Next, we store a whole dataset at once, in Matrices: A Whole Dataset at Once. See you there.

## Thumbnail
Headline: One Number, Many Features
Image: Navy background, two short vectors meeting in a single teal number 31, headline in teal Inter Bold.

## Production Notes
- [VERSION] NumPy: np.dot is stable, but confirm its behaviour and any warnings against the current NumPy version before recording. content.md outputs were checked with NumPy 2.4.
- All numbers (Dewi's delivery weights of 2 minutes per kilometre and 5 minutes per stop, the taste scores) are hypothetical and must not be presented as real data. Dewi and the Jakarta start-up are fictional; no real courier brand or logo in stock footage.
- Not a screen demo lesson: code appears only on code slides.
