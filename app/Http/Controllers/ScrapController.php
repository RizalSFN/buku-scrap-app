<?php

namespace App\Http\Controllers;

use App\Models\Buku;
use Illuminate\Http\Request;

class ScrapController extends Controller
{
    public function index()
    {
        $books = Buku::paginate(10);
        return view('index', compact('books'));
    }
}
