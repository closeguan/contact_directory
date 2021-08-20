#!"C:\Strawberry\perl\bin\perl.exe" 

use strict;
use warnings;
use DBI;
use JSON;
use Encode;
use CGI qw(:standard);

print header(-charset => 'utf-8'); # 定義表頭，並給utf8編碼
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
### SQL query here
my $sth = $dbh->prepare("SELECT * FROM list");
 
### execute the query
$sth->execute( );



my @output;          # fetchrow_hashref()
while(my $ref = $sth->fetchrow_hashref()) {  # 取特定欄位  #$sth->fetchrow_array( )
  push @output, $ref;
  
}


$dbh->disconnect();

#my $JSON=encode_json( {myData => \@output } );
my $JSON=encode_json(  \@output );
print  $JSON;



