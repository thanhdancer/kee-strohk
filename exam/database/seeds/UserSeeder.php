<?php

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class UserSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        factory(App\User::class, 50)->create()->first()->update([
        	'email' => 'hiendv@keystroke.dev',
        	'password' => Hash::make('hiendv'),
        ]);
    }
}
