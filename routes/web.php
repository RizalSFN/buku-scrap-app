<?php

use App\Http\Controllers\ScrapController;
use Illuminate\Support\Facades\Route;

Route::get('/', [ScrapController::class, 'index'])->name('index');
