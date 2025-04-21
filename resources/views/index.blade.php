<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Buku Application</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>

<body>
    <h1 class="w-full text-center font-bold text-2xl py-4">DATA BUKU TOP SELLER 2025</h1>
    <table class="mt-2 border border-gray-200 text-center w-full">
        <thead>
            <tr class="bg-gray-200 text-neutral-400 font-medium text-sm">
                <td class="w-1/12 py-3">ID</td>
                <td class="w-1/12 py-3">IMAGES</td>
                <td class="w-1/12 py-3">TITLE</td>
                <td class="w-2/12 py-3">AUTHOR</td>
                <td class="w-2/12 py-3">RATING</td>
                <td class="w-2/12 py-3">SCORE</td>
            </tr>
        </thead>
        <tbody>
            @foreach ($books as $book)
                <tr class="border-b border-gray-200">
                    <td class="py-3">{{ $book->id }}</td>
                    <td class="py-3"><img src="{{ $book->images }}" alt="{{ $book->title }}"></td>
                    <td class="py-3">{{ $book->title }}</td>
                    <td class="py-3">{{ $book->authors }}</td>
                    <td class="py-3">{{ $book->ratings }}</td>
                    <td class="py-3">{{ $book->scores }}</td>
                </tr>
            @endforeach
        </tbody>
    </table>
</body>

</html>
