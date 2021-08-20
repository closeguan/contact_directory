#!"C:\Strawberry\perl\bin\perl.exe" 

use strict;
use warnings;
use DBI;
use JSON;
use Encode;
use CGI qw(:standard);

print header(-charset => 'utf-8'); # 定義表頭，並給utf8編碼

## input from ajax
my $cgi = CGI->new;
my	$user = $cgi->param('user'); 
my  $name = $cgi->param('name');
my  $email = $cgi->param('email');
my  $phone = $cgi->param('phone');

## test data
#my	$user = "test001";  # &>=
#my  $name = "測試123";
#my  $email = "test001\@gmail.com";
#my  $phone = "122102";

my @array = ($user, $name, $email, $phone);


### MySQL connect details
my $db = "project";
my $host = "localhost";
my $username = "root";
my $password = "1234";
 
### connect to MySQL database
my $dbh = DBI->connect ("DBI:mysql:database=$db:host=$host", $username, $password) 
						or die "Could not connect to database: $DBI::errstr\n";
$dbh->{mysql_enable_utf8} = 1;
$dbh->do('set names "UTF8"');


##########################################
#    insert data into the list table
##########################################
my $table="list";
my $sql  = "INSERT INTO $table(user,name,email,phone) VALUES(?,?,?,?)";
my $stmt = $dbh->prepare($sql);
$stmt->execute($array[0], $array[1], $array[2], $array[3]);

##  after insert : select all t print
$stmt->finish();

#error

#convert  data to JSON
my $op = JSON -> new -> utf8 -> pretty(1);
my $json = $op -> encode({
    emailPERL => $email,
    userPERL => $user,
	namePERL => $name,
	phonePERL => $phone,
});

print $json;



