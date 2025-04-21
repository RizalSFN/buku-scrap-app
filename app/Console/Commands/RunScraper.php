<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;

class RunScraper extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'app:run-scraper';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Command description';

    /**
     * Execute the console command.
     */
    public function handle()
    {
        $output = shell_exec('python3 ' . public_path('scrap/scrapping-data-web.py'));
        $this->info($output);
    }
}
