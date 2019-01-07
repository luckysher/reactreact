

const e = React.createElement;

function TopHeading(p){
    return <h2 className={p.c}>{p.t}</h2>;
}

function NavHeading(p){
    return <div className="navbar-header">
          <button type="button" className="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
            <span className="icon-bar"></span>
            <span className="icon-bar"></span>
            <span className="icon-bar"></span>
          </button>
          <a className="navbar-brand" href="#">{p.heading}</a>
        </div>;

}
