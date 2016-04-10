<?php

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class AssignmentSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        factory(App\Assignment::class, 30)->create();
    }
}
